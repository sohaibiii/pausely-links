// Cloudflare serves every page and file in this repository straight from its
// static assets, without running this script. The one exception is the demo
// video: Cloudflare's static assets answer a byte-range request with the whole
// file, and Safari on iPhone refuses to play a video from a server that does
// that. So requests under /assets/video/ come here first, and this script cuts
// the requested bytes out of the file.

export default {
	async fetch(request, env) {
		const range = request.headers.get("Range");
		const method = request.method;
		if (!range || (method !== "GET" && method !== "HEAD")) {
			return withAcceptRanges(await env.ASSETS.fetch(request));
		}

		// Ask for the whole file, keeping the validators so a 304 still works.
		const headers = new Headers(request.headers);
		headers.delete("Range");
		headers.delete("If-Range");
		const full = await env.ASSETS.fetch(new Request(request.url, { method: "GET", headers }));
		if (full.status !== 200) {
			return full;
		}

		// If-Range: serve the range only if the visitor's copy is still current.
		const ifRange = request.headers.get("If-Range");
		if (ifRange && ifRange !== full.headers.get("ETag")) {
			return withAcceptRanges(full);
		}

		const bytes = await full.arrayBuffer();
		const size = bytes.byteLength;
		const span = parseRange(range, size);
		if (span === null) {
			// Not a single byte range we understand: the whole file is a valid answer.
			return withAcceptRanges(new Response(method === "HEAD" ? null : bytes, full));
		}

		const out = new Headers(full.headers);
		out.set("Accept-Ranges", "bytes");
		if (span === false) {
			out.set("Content-Range", `bytes */${size}`);
			out.delete("Content-Length");
			return new Response(null, { status: 416, headers: out });
		}

		const [start, end] = span;
		out.set("Content-Range", `bytes ${start}-${end}/${size}`);
		out.set("Content-Length", String(end - start + 1));
		return new Response(method === "HEAD" ? null : bytes.slice(start, end + 1), {
			status: 206,
			headers: out,
		});
	},
};

// "bytes=0-1", "bytes=100-" or "bytes=-500". Returns [start, end], false when the
// range lies outside the file, or null when it is not one plain byte range.
function parseRange(value, size) {
	const match = /^bytes=(\d*)-(\d*)$/.exec(value.trim());
	if (!match || (match[1] === "" && match[2] === "")) {
		return null;
	}
	if (size === 0) {
		return false;
	}
	if (match[1] === "") {
		const length = Number(match[2]);
		if (length === 0) {
			return false;
		}
		return [Math.max(0, size - length), size - 1];
	}
	const start = Number(match[1]);
	const end = match[2] === "" ? size - 1 : Math.min(Number(match[2]), size - 1);
	if (start >= size || start > end) {
		return false;
	}
	return [start, end];
}

function withAcceptRanges(response) {
	if (response.status !== 200) {
		return response;
	}
	const headers = new Headers(response.headers);
	headers.set("Accept-Ranges", "bytes");
	return new Response(response.body, { status: response.status, headers });
}

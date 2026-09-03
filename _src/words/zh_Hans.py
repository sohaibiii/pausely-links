# -*- coding: utf-8 -*-
"""简体中文。和 App 一样，用“你”。"""

COPY = {

"nav.support": "帮助",
"nav.about": "关于",
"nav.privacy": "隐私",
"nav.terms": "条款",
"nav.data": "你的数据",

"ui.skip": "跳到正文",
"ui.pages": "页面",
"ui.footer": "页脚",
"ui.lang": "语言",
"ui.toc": "本页内容",
"ui.rights": "保留所有权利。",
"ui.store_soon": "即将上架 App Store",
"ui.store_get": "在 App Store 下载",
"ui.date": "2026年9月3日",
"ui.last_updated": "最后更新：{DATE}",

"k.settings": "设置",
"k.your_data": "你的数据",
"k.reset_all": "重置全部数据",
"k.restore": "恢复购买",
"k.screen_time": "屏幕使用时间",
"k.apps_with_st": "可访问“屏幕使用时间”的 App",
"k.notifications": "通知",
"k.ai_reflection": "AI 反思",
"k.what_is_sent": "发送的内容",
"k.language": "语言",
"k.premium": "Premium",
"k.protection": "保护",

"meta.support.title": "Pausely — 帮助",
"meta.support.desc": "Pausely 官方帮助。它会在你选中的 App 前放上一次暂停。工作方式、运行要求、常见问题与联系方式。",
"meta.about.title": "Pausely — 滑动之前，先喘口气",
"meta.about.desc": "Pausely 在你和那些吃掉你一天的 App 之间放了一道小小的减速带。没有账号，除非你开口，什么都不会离开你的设备。",
"meta.privacy.title": "隐私政策 — Pausely",
"meta.privacy.desc": "Pausely 留在你设备上的东西、唯一会发送内容的可选功能，以及它究竟发送什么。",
"meta.terms.title": "使用条款 — Pausely",
"meta.terms.desc": "Pausely 使用条款（EULA）：这个 App 是什么、不是什么，Premium 如何计费，以及严格模式对你的要求。",
"meta.data.title": "删除你的数据 — Pausely",
"meta.data.desc": "如何抹掉 Pausely 拥有的一切——它们全都在你的设备上——以及订阅会怎样。",
"meta.nf.title": "未找到 — Pausely",
"meta.nf.desc": "页面未找到。",

"s.eyebrow": "帮助",
"s.h1": "Pausely 使用帮助",
"s.sub": "滑动之前，先喘口气。Pausely 会站在你选中的 App 前面，先向你要十秒钟。本页说明它如何工作、需要什么，以及怎样联系我们。",
"s.cta": "阅读常见问题",
"s.meta": '没有账号 · 除非你开口，什么都不会离开你的设备 · <a href="{BASE}{L}/privacy/">隐私政策</a>',

"s.how.h": "Pausely 如何工作",
"s.how.b": """
<p class="lead">Pausely 在你和那些吃掉你一天的 App 之间放了一道小小的减速带。</p>
<p>你来挑选那些希望少用一点的 App。此后，点开它们不会立刻进入——Pausely 会先站在前面，给你一次短短的暂停：一次呼吸、一句要打的话，或者一个关于“你为什么要打开它”的提问。如果你还是想进去，你可以，但只有一段限定的时间。时间结束，暂停就回来了。</p>
<p>目的不是把你锁在门外，而是把拇指主导的自动习惯，变成一个你真正做出的决定。给上十秒去想，多数人会把 App 关掉——Pausely 会把这算作一次成功。</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>保护</b><span>一个开关。打开的时候，你选中的 App 不会打开，而是显示 Pausely 那块平静的拦截屏。</span></div></li>
  <li><span class="tile">{wind}</span><div><b>三种暂停</b><span>一次呼吸练习、一道打字题，或者写下你的意图。设置过程会挑一个适合你的，你随时可以更换。</span></div></li>
  <li><span class="tile">{clock}</span><div><b>规则</b><span>在特定时段守住特定的 App——睡前、工作日——各有各的暂停和各自的时长。规则也可以在时段结束前完全拦住。</span></div></li>
  <li><span class="tile">{lock}</span><div><b>严格模式</b><span>让自己守住一小时、一天，或直到你选定的时刻。它运行期间，保护关不掉，规则也删不了——连你自己也不行。</span></div></li>
  <li><span class="tile">{book}</span><div><b>替代选项与日志</b><span>最多三个健康的替代选项会出现在暂停屏上，作为第三条出路；还有一本日志，留给那些你更想写点什么、而不是划屏的时候。</span></div></li>
  <li><span class="tile">{chart}</span><div><b>进展</b><span>守住的暂停、夺回的时间、连续记录和每周图表——还有主屏幕小组件，以及解锁时段开着时锁屏上的倒计时。</span></div></li>
  <li><span class="tile">{sparkle}</span><div><b>AI 反思，如果你想要的话</b><span>在你打开它之前一直关着。它把“你为什么要打开它？”变成一小段对话，还会写一段关于你这一周的小结。这是 Pausely 里唯一用到网络的部分——见<a href="{BASE}{L}/privacy/#ai">隐私</a>。</span></div></li>
</ul>
""",

"s.requirements.h": "运行要求",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>设备</th><td>运行 <strong>iOS 17 或 iPadOS 17</strong> 及更新系统的 <strong>iPhone 或 iPad</strong>。一个 App、一套布局，两种设备通用。</td></tr>
<tr><th>权限</th><td><strong>“屏幕使用时间”</strong>访问权限，在设置过程中通过 Apple 自己的弹窗授予一次。Pausely 使用 Apple 的“屏幕使用时间”框架——就是 iOS 内置 App 限额背后的那套系统——真正拦住 App 的是 Apple，不是 Pausely。</td></tr>
<tr><th>账号</th><td>不需要。App 里没有任何注册、邮箱输入框或密码。</td></tr>
<tr><th>网络</th><td>不需要。每一次暂停、每条规则、每张图表和每篇日志都能离线使用。只有两件事会用到网络：你购买或恢复 Premium 时 Apple 自己的通信，以及 AI 反思——它在你打开之前一直关着。</td></tr>
<tr><th>通知</th><td>可选，且只在设备本地产生。Pausely 用它把你从拦截屏交接到暂停，并在结束后问你这一段让你感觉如何。这里没有推送服务器。</td></tr>
<tr><th>语言</th><td>英语、德语、西班牙语、法语、日语、韩语、巴西葡萄牙语和简体中文。Pausely 跟随设备的语言，你也可以在{K_settings} → {K_language}里另选一种。</td></tr>
</table></div>
""",

"s.start.h": "开始使用",
"s.start.b": """
<p>设置一共七屏，用不到三分钟。走完的时候，保护已经打开，第一条规则也已经写好。</p>
<ol class="steps">
  <li><div><b>说说一天里有多少时间给了手机</b>——你自己的估计，不是测出来的数字。</div></li>
  <li><div>Apple 询问时<b>允许访问“屏幕使用时间”</b>。没有它 Pausely 无法工作，你也可以随时在{K_settings} → {K_screen_time}中收回。</div></li>
  <li><div>在 Apple 的选择器里<b>挑出你的 App</b>。Pausely 永远不会知道它们的名字——见<a href="{BASE}{L}/privacy/">隐私</a>。</div></li>
  <li><div><b>回答三个问题</b>，由它们挑出适合你的暂停。</div></li>
  <li><div><b>添加最多三个替代选项</b>——散步、看书、一杯水，或者你自己的、能跳转到另一个 App 的选项。</div></li>
  <li><div><b>完成。</b>打开你选中的一个 App，去见见那次暂停。</div></li>
</ol>
""",

"s.faq.h": "常见问题",
"s.faq.b": """
<dl class="faq">
<dt>Pausely 免费吗？</dt>
<dd>免费。免费版是一个能用的产品，不是演示：<strong>一条规则</strong>、<strong>呼吸暂停</strong>，以及<strong>完整的进展页面</strong>——暂停、成功、夺回的时间、连续记录和图表。</dd>
<dt>Premium 多了什么？</dt>
<dd>规则想建多少建多少，另外两种暂停（输入才能继续、写下你的意图），严格模式，把“用完之后的感受”和“转身离开之后的感受”放在一起看的心情分析，以及可选的 AI 反思和它的每周小结。Premium 是按月或按年的订阅——年度方案以<strong>免费试用</strong>开始——或者一次性的永久购买。价格显示在 App 内和你所在国家/地区的 App Store，账单由 Apple 处理。</dd>
<dt>订阅到期了会怎样？</dt>
<dd>你搭起来的东西一样都不会被拿走。每条规则照常运行，也仍然可以编辑，你选的那种暂停也照旧站在 App 前面。关上的只是“再添加更多”这件事。一个因为卡过期就不再守护你手机的 App，恰恰是在你请它别这么做的那一刻辜负了你。</dd>
<dt>能在新设备上恢复购买吗？</dt>
<dd>可以。打开 Premium 页面，点按{K_restore}。Premium 属于你的 Apple 账户，而不是某台设备。</dd>
<dt>为什么 Pausely 不能告诉我拦住了哪些 App？</dt>
<dd>因为它真的不知道。Apple 的“屏幕使用时间”交给 Pausely 的是不透明的令牌，离开你的设备就毫无意义——没有 App 名称，也没有标识符。Pausely 可以请 iOS 去拦住它们，却读不出它们是什么。</dd>
<dt>我关不掉保护，是坏了吗？</dt>
<dd>看看<strong>严格模式</strong>是不是正在运行——主页面会写明。它运行期间，保护关不掉、规则删不了，这是有意为之。到了你选定的时刻，它会自己结束。</dd>
<dt>Pausely 会看到我在别的 App 里做什么吗？</dt>
<dd>不会。它从不观察你的浏览、你的消息，或你在任何 App 内的活动。它只记录自己的事件——一次暂停被显示过，以及你选择了什么——而这些也留在你的设备上。</dd>
<dt>AI 反思是什么？它开着吗？</dt>
<dd>关着，直到你打开它。打开之后，其中一次暂停会变成一小段对话：你写下为什么要打开这个 App，回来的是一个问题。它还会写一段关于你这一周的短文。这些文字会送到 Pausely 自己的服务器，再到运行模型的 Google——你的日志、你的心情记录、你选了哪些 App，都不会。{K_settings} → {K_ai_reflection} → {K_what_is_sent}里列出了每一个字段；把它关掉，App 就回到完全不发起任何网络请求的状态。</dd>
<dt>iPad 上能用吗？Mac 呢？</dt>
<dd>iPad 可以：Pausely 是一个同时面向 iPhone 和 iPad 的 App，两边布局一致，也支持分屏浏览、侧拉和台前调度。Mac 不行：Pausely 所依赖的“屏幕使用时间”框架在那里并不存在。</dd>
<dt>可以用我自己的语言阅读吗？</dt>
<dd>Pausely 会说八种语言，并跟随设备的设置。想换一种来读——又不改动设备上的其他东西——就打开{K_settings} → {K_language}。拦截屏、小组件和锁屏也都会跟着这个选择走。</dd>
<dt>怎样把一切都抹掉？</dt>
<dd>{RESET}。这会清空每一次暂停、每一次成功、每条规则、每篇日志和每次心情记录，撤下拦截，把你带回起点。严格模式运行时它会拒绝执行。详情见<a href="{BASE}{L}/delete-data/">你的数据</a>页面。</dd>
</dl>
""",

"s.trouble.h": "排查问题",
"s.trouble.b": """
<h3>App 没有暂停就打开了</h3>
<ul>
  <li>检查主页面上的<strong>保护</strong>开关。</li>
  <li>检查“屏幕使用时间”的访问权限是否仍然有效：{K_settings} → {K_screen_time} → {K_apps_with_st}。如果被收回了，Pausely 会显示一个带按钮的恢复页面，可以再次申请。</li>
  <li>如果这个 App 只写在某条<strong>规则</strong>里，暂停只会在那条规则的时段出现。</li>
  <li>你早些时候开启的<strong>解锁时段</strong>可能还在走——锁屏上的倒计时会显示还剩多久。</li>
</ul>
<h3>拦截屏出现了，但暂停始终不打开</h3>
<ul>
  <li>点按拦截屏上的按钮，会通过一条通知把你交接过去。如果 Pausely 的通知是关的，iOS 就无法送达这次交接——请在{K_settings} → {K_notifications} → <kbd>Pausely</kbd>中打开。</li>
  <li>直接打开 Pausely，也会打开正在等待的那次暂停。</li>
</ul>
<h3>小组件慢了半拍</h3>
<p>iOS 按自己的节奏刷新小组件。打开 Pausely，它们会立刻更新。</p>
<h3>App 显示成了别的语言</h3>
<p>打开{K_settings} → {K_language}，选你想要的那种。Pausely 自己绘制的一切会立刻跟上。Apple 的 App 选择器由 iOS 绘制、而非 Pausely，所以要到下次启动才会改变。</p>
<h3>Premium 没被识别</h3>
<p>在 Premium 页面点按{K_restore}，并确认设备登录的是当初购买时的同一个 Apple 账户。退款和账单问题由 Apple 通过 <a href="https://support.apple.com/billing">Apple 支持</a>处理。</p>
""",

"s.contact.h": "联系我们",
"s.contact.b": """
<p>有疑问、遇到问题，或者某件本该好用的事情不好用——写信给我们，会有人回复。</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">请附上设备型号、iOS 版本，以及你原本期待发生什么。千万不要把日志或心情记录发给我们——我们不需要，也不愿意保管它们。</span></div></div>
<p style="margin-top:16px" class="small">账单、退款和订阅变更由 Apple 处理：<a href="https://apps.apple.com/account/subscriptions">管理订阅</a> · <a href="https://support.apple.com/billing">申请退款</a>。</p>
""",

"a.eyebrow": "关于 Pausely",
"a.h1": "滑动之前，先喘口气。",
"a.sub": "挑出那些你希望少用一点的 App。此后，打开其中一个，先迎来一次暂停——以及一个你真正做出的选择。",
"a.cta": "帮助",
"a.meta": "没有账号 · iPhone 和 iPad · iOS 17 及以上 · 八种语言",
"a.lead": "Pausely 在你和那些吃掉你一天的 App 之间放了一道小小的减速带。不是上锁，也不是说教——只是十秒钟，让你确认自己是不是真的想打开。",

"a.f1.h": "滑动之前，先喘口气。",
"a.f1.p": "Pausely 会站在你选中的 App 前面，先向你要十秒钟——一次呼吸练习、一句要打的话，或者一小会儿，用来写下你的意图。",
"a.f2.h": "你为什么要打开它？",
"a.f2.p": "把条件反射变成决定——并且是有意做出的决定。多数时候，只要有机会想一想，人们就会把 App 关掉。",
"a.f3.h": "转身离开也算数。",
"a.f3.p": "把这次成功留下，或者进去五分钟——不上锁，也不说教。你自己设的替代选项就摆在暂停屏上，作为第三条出路。",
"a.f4.h": "看着时间回来。",
"a.f4.p": "每一次守住的暂停、每一个夺回的小时、连续记录和每周图表——还有主屏幕小组件和锁屏上的倒计时。",
"a.f5.h": "你的 App，你的规则。",
"a.f5.p": "给每个 App 一个开关和一种暂停，还有为夜晚和工作日准备的时间表。只要你开口，严格模式会把你按在自己的承诺上。",
"a.f6.h": "什么都不会离开你的设备。",
"a.f6.p": '没有账号、没有分析统计、没有广告。连你挑了哪些 App，Pausely 都读不出来——那是 Apple 保管的。只有一个可选功能会发送内容，而它一开始就是关着的。<a href="{BASE}{L}/privacy/">看看这是怎么做到的。</a>',

"a.price.h": "价格",
"a.price.b": """
<p>免费版是一个能用的产品，不是演示；你设好的东西也永远不会被拿走——哪怕订阅到期。</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">免费</div><div class="price">￥0</div><ul><li>一条规则</li><li>呼吸暂停</li><li>完整的进展页面——成功、夺回的时间、连续记录和图表</li><li>小组件与锁屏倒计时</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">按月 · 按年 · 永久</div><ul><li>规则想建多少建多少</li><li>三种暂停全部解锁</li><li>严格模式</li><li>心情分析</li><li>可选的 AI 反思及其每周小结</li><li>年度方案以免费试用开始</li></ul></div>
</div>
<p class="small" style="margin-top:14px">价格显示在 App 内和你所在国家/地区的 App Store。账单由 Apple 处理。<a href="{BASE}{L}/terms/#subscriptions">订阅条款。</a></p>
""",

"a.st.h": "建立在 Apple 的“屏幕使用时间”之上",
"a.st.b": """
<p>Pausely 使用的，正是驱动 iOS 内置 App 限额的那套框架。Apple 只会把它交给为此用途审核过的 App，而真正挡在你和 App 之间的是 Apple，不是 Pausely。也正因为如此，Pausely 才能在从不知道名字的情况下拦住一个 App。</p>
<ul class="rows" style="margin-top:16px">
  <li><span class="tile">{tablet}</span><div><b>iPhone 和 iPad，同一个 App</b><span>两边都是同样的单列布局，在分屏浏览、侧拉和台前调度里也都规规矩矩。iOS 17 或 iPadOS 17 及以上。</span></div></li>
  <li><span class="tile">{globe}</span><div><b>八种语言</b><span>英语、德语、西班牙语、法语、日语、韩语、巴西葡萄牙语和简体中文——拦截屏和小组件也包括在内。在{K_settings} → {K_language}里选一种，不必改动设备上的其他设置。</span></div></li>
</ul>
""",

"p.eyebrow": "隐私政策",
"p.h1": "它知道的，留在你的设备里。",
"p.sub": "Pausely 没有账号，也没有分析统计。它记录的一切都留在你的设备上——只有一个可选功能例外，它在你开口之前一直关着，会发送你在某一个屏幕上打下的文字。这一页讲的就是这条界线到底划在哪里。",
"p.meta": "自 {DATE} 起生效 · 适用于 iPhone 和 iPad 版 Pausely App，以及本网站",

"p.summary.h": "简短版本",
"p.summary.b": """
<p class="lead">Pausely 没有账号、没有分析统计、没有广告，也没有任何第三方代码。<strong>在 AI 反思关闭时——每一次安装都是这样开始的——它完全不发起任何网络请求</strong>，它知道的一切都写在你的设备上，并留在那里。</p>
<p><strong>打开 AI 反思是唯一会改变这一点的事</strong>，而它只改变一件事：你在那一次暂停里打下的文字，会连同关于那一刻的四个小事实一起离开你的设备。你的日志永远不会离开。你的心情记录永远不会离开。你选了哪些 App 也不会离开——因为哪怕在你自己的设备上，Pausely 都读不出它。</p>
<div class="callout"><span class="tile">{eye-off}</span><div>Pausely 不知道你选了哪些 App 来加暂停。Apple 的“屏幕使用时间”给它的是不透明的令牌，只有你的设备能解读。没有 App 名称，没有标识符，也没有可以发送的东西。</div></div>
<p style="margin-top:16px">本政策适用于由 {COMPANY} 发行的 iPhone 和 iPad 版 Pausely App，以及本网站。它与 Pausely 在 App Store 页面上的隐私标签说的是同一件事：<strong>用户内容，不与你的身份关联，仅用于让 App 正常运作——且没有追踪。</strong>这唯一的一条标签是因为 AI 反思才存在的；其余每一个类别都是<em>未收集数据</em>。</p>
""",

"p.collect.h": "我们收集什么",
"p.collect.b": """
<p>“收集”，无论按 Apple 的定义还是我们的定义，都是指把数据传出设备，并保存在某个非临时的地方。以这个标准衡量，Pausely 收集的只有一样东西、只在一种情形下，而且只有在你主动要求时才会发生。</p>
<div class="table-wrap"><table>
<tr><th>类别</th><th>是否收集？</th><th>这意味着什么</th></tr>
<tr><td>联系信息</td><td>否</td><td>App 里没有任何账号、登录或邮箱输入框。</td></tr>
<tr><td>标识符</td><td>否</td><td>没有用户 ID、设备 ID 或广告标识符。Pausely 从不申请 App 跟踪透明度权限，因为它根本没有要问的事。</td></tr>
<tr><td>使用数据</td><td>否</td><td>没有分析 SDK，也没有交互事件。除了你自己的进展页面，任何地方都不会计数，而那也只在你的设备上。</td></tr>
<tr><td>用户内容</td><td><strong>仅 AI 反思</strong></td><td>你的日志、心情记录和自定义替代选项都保存在设备上，别无他处。只有当你打开 AI 反思时——也仅在那时——你在<em>那一个屏幕</em>上打下的文字才会被发送，好让一个问题能返回给你。你写下的其他任何内容都永远不会被发送。</td></tr>
<tr><td>购买</td><td>否</td><td>付款是 Apple 的事，发生在 App Store 的面板里。Pausely 从不接触银行卡，也不会把购买相关的任何信息发往任何地方。</td></tr>
<tr><td>位置、健康、通讯录、浏览、搜索、诊断</td><td>否</td><td>能读取这些内容的框架，Pausely 根本没有链接；它也没有自己的崩溃或性能上报。</td></tr>
</table></div>
<p style="margin-top:14px"><strong>追踪：</strong>没有。Pausely 不会把与你有关的任何内容，同其他公司的 App 或网站的数据关联起来，也不会与数据经纪商或广告商共享任何东西。App 内没有广告，也没有任何能夹带广告的 SDK。</p>
""",

"p.device.h": "留在你设备上的东西",
"p.device.b": """
<p>Pausely 把以下内容保存在你 iPhone 或 iPad 上属于它自己的私有存储里，由设备的密码和加密保护。这些都不会被上传，我们不会备份，也看不到。</p>
<ul>
  <li><strong>你选中的 App</strong>——以 Pausely 读不出内容的不透明“屏幕使用时间”令牌形式保存（见下文）。</li>
  <li><strong>你的规则和时间表</strong>——你给它们起的名字、时段，以及使用哪种暂停。</li>
  <li><strong>暂停的结果</strong>——一次暂停被显示过、发生在什么时候，以及你是转身离开、进去了，还是选了替代选项。进展页面、连续记录和图表都是由这些构成的。</li>
  <li><strong>你写下的东西</strong>——日志、你在暂停屏上打下的文字、一段使用之后的心情记录，以及自定义替代选项的名字。</li>
  <li><strong>设置</strong>——你选的暂停、严格模式的状态、替代选项、你的语言，以及各种偏好。</li>
  <li><strong>你的 Premium 权益</strong>——一个等级和一个到期日期，好让 App 知道该解锁什么。</li>
</ul>
<p>如果你使用 iCloud 备份或加密的本地备份，Apple 可能会把 Pausely 的数据包含在那份备份里；它归属于你自己的 Apple 账户，受 Apple 的隐私条款约束。我们无法访问它。</p>
""",

"p.screentime.h": "“屏幕使用时间”与你选中的 App",
"p.screentime.b": """
<p>Pausely 建立在 Apple 的“屏幕使用时间”框架之上（Family Controls、Managed Settings 和 Device Activity）。你通过 Apple 自己的弹窗授权一次，并可随时在{K_settings} → {K_screen_time}中收回。</p>
<p>当你挑选 App 时，Apple 的选择器返回的是<strong>令牌</strong>：这些值能向 iOS 指明是哪个 App，但对 Pausely 毫无意义，离开你的设备也毫无意义。Pausely 保存这些令牌，只是为了能请 iOS 去遮住你选中的 App。它从不会收到 Bundle 标识符或 App 名称，就算它想上报也做不到。当它需要在自己的各个组件之间比对令牌时，比对的是单向哈希，而不是令牌本身。</p>
<p>Pausely 不会观察你的浏览、你的消息，或你在任何 App 内的行为。绘制拦截屏并执行遮挡的是 iOS 自己。Pausely 只知道自己的那次暂停被显示过，以及你在上面选了什么。</p>
""",

"p.ai.h": "AI 反思——唯一会出去的东西",
"p.ai.b": """
<p class="lead">这是一个可选的 Premium 功能。<strong>你安装 Pausely 时它是关着的，并且会一直关着，直到你打开它</strong>；再把它关掉，App 就回到完全不发起任何网络请求的状态。</p>
<p>打开之后，其中一次暂停会变成一小段对话：你写下为什么要打开这个 App，回来的是一个问题，而不是一通说教。每周一次，它还会写一段关于你这一周过得如何的短文。</p>
<h3>会发送什么</h3>
<ul>
  <li><strong>你正要打开的那个 App 的显示名称</strong>——那一刻本来就已经在你屏幕上的名字。</li>
  <li><strong>三个数字</strong>：你今天打开过它几次、现在几点，以及你的连续记录有多长。</li>
  <li><strong>你在那个屏幕上打下的文字</strong>，就在那一刻。</li>
</ul>
<p>每周小结发送的更少：只有这一周的计数，别无其他。里面完全不会出现任何 App 名称。</p>
<h3>永远不会发送什么</h3>
<ul>
  <li><strong>你的日志。</strong>那是你为了不给任何人看而书写的唯一地方，它从不离开设备。</li>
  <li><strong>你的心情记录</strong>、心情本身，或附在上面的任何备注。</li>
  <li><strong>你选中的 App</strong>——你守着哪些、守了几个——也从不发送“屏幕使用时间”令牌、令牌哈希或 Bundle 标识符。</li>
  <li><strong>你的规则、时间表或严格模式的状态。</strong></li>
  <li><strong>任何能指认出你的东西。</strong>没有账号、没有用户 ID、没有广告标识符可供发送。请求会带上 Apple 的 App Attest 证明，它只是告诉我们的服务器：对面是一份货真价实的 Pausely。它绑定的是这个 App，不是你，也不会跨请求跟着你。</li>
</ul>
<h3>去到哪里，留多久</h3>
<p>你的文字会送到 <strong>Pausely 自己的服务器</strong>，再到运行模型的 <strong>Google</strong>。Pausely 从不从你的设备直接调用任何模型厂商的 API，App 里也没有可以被掏出来的 API 密钥。</p>
<p><strong>Pausely 的服务器对每次请求什么都不保存</strong>——不保存提问、不保存回答、不保存上下文。它的日志只记下一次请求的形状（时间戳、耗时、是否成功），从不记录内容。<strong>Google 会把输入和输出保留最多 24 小时</strong>，用于降低延迟，并可能依据其标准的 Cloud 条款检查输入是否存在滥用。<strong>这些内容 Google 都不会用来训练模型。</strong></p>
<p>{K_settings} → {K_ai_reflection} → {K_what_is_sent}在 App 内列出了每一个字段，用词与本页相同。</p>
""",

"p.purchases.h": "购买",
"p.purchases.b": """
<p>Premium 通过 Apple 的 App Store、使用 StoreKit 出售。这笔交易发生在你和 Apple 之间，适用 <a href="https://www.apple.com/legal/privacy/">Apple 的隐私政策</a>。Apple 只告诉 Pausely 某项购买是否有效——仅此而已——而 Pausely 也不会把你如何使用 App 的任何信息告诉 Apple。没有使用数据、没有日志、没有 App 选择、也没有我们这边的任何标识符会随一次购买一起流动。</p>
""",

"p.notifications.h": "通知、小组件与锁屏",
"p.notifications.b": """
<p><strong>通知</strong>是可选的，并且在你的设备上生成。Pausely 用它把你从拦截屏交接到暂停，并在结束后问你这一段让你感觉如何。没有任何通知来自服务器——这里没有推送服务器，没有小贴士，没有连续记录的催促，也没有营销。</p>
<p><strong>小组件和实时活动</strong>显示的是计数和时间——今天的成功、你的连续记录、夺回的时间，以及一个解锁时段还剩多久。它们被刻意设计成没有“屏幕使用时间”权限，永远看不到你拦住了哪些 App。锁屏上的倒计时说出的是你写下的<em>规则</em>名称（“睡前”），而不是 App 名称，因为锁屏是任何拿到设备的人都能读到的。</p>
""",

"p.third.h": "第三方",
"p.third.b": """
<p>Pausely 里<strong>没有第三方代码</strong>：没有分析统计、没有广告、没有崩溃上报、没有 SDK。参与其中的只有另外两方，也仅有这两方：</p>
<ul>
  <li><strong>Apple</strong> 运营 App Store、处理购买、执行“屏幕使用时间”的遮挡；如果你已同意与开发者共享，它还可能依据自身政策向我们提供崩溃日志。</li>
  <li><strong>Google</strong> 运行 AI 反思背后的模型，且仅在你打开该功能期间。它收到的只有上面列出的内容，别无其他，也不会用来训练自己的模型。</li>
</ul>
<p>我们不向任何人出售或出租个人数据，也不与数据经纪商或广告商共享任何东西。</p>
""",

"p.delete.h": "删除你的数据",
"p.delete.b": """
<p>Pausely 拥有的一切，都可以在 App 内抹掉，不必来问我们：</p>
<div class="callout"><span class="tile">{trash}</span><div>{RESET}<br><span class="small">清空每一次暂停、每一次成功、每条规则、每篇日志和每次心情记录，撤下遮挡，收回时间表，把你带回起点。严格模式运行时它会拒绝执行——那是你请这个 App 替你守住的唯一一个承诺——而且它不会动你的订阅，那属于你的 Apple 账户。</span></div></div>
<p style="margin-top:16px">删除 App，也会把它在设备上的全部数据一并带走。我们这边没有可删的东西：服务器在回答完一次请求之后，不会留下关于它的任何记录。你仍然随时可以写信给我们——见<a href="{BASE}{L}/delete-data/">你的数据</a>页面。</p>
""",

"p.rights.h": "你的权利",
"p.rights.b": """
<p>无论你住在哪里——包括在 GDPR、英国 GDPR 和 CCPA/CPRA 之下——你都有权访问、更正、导出、限制和删除一家公司持有的关于你的个人数据，并向监管机构投诉。Pausely 没有关于你的任何画像，一次反思被回答之后也不留下任何东西，所以我们这边既没有可以提供的，也没有可以删除的；你设备上的数据本来就在你手里，而 App 自己的操作就替你行使了上述每一项权利。如果你认为并非如此，请写信到 {MAIL}，我们会回复。</p>
""",

"p.children.h": "儿童",
"p.children.b": """
<p>Pausely 是给使用这台设备的人自己用的、自我约束的工具。它不是家长控制产品，也不管理别人的设备。它不面向 13 岁以下儿童（或你所在地区规定的数字同意年龄以下的人），我们也不会有意收集任何人的个人信息——无论年龄。</p>
""",

"p.changes.h": "本政策的变更",
"p.changes.b": """
<p>随着 App 的变化，我们可能会更新本政策。更新时顶部的日期会一并变动，重要变更会写进 App 的版本说明。上一次实质性变更是 AI 反思的到来，它带来了“有东西离开你的设备”的唯一一种情形。变更之后继续使用 Pausely，即表示你接受修订后的政策。</p>
""",

"p.contact.h": "联系我们",
"p.contact.b": """
<p>Pausely 的发行方 {COMPANY} 是此处所涉一切内容的控制者。隐私相关问题请联系：{MAIL}。</p>
""",

"t.eyebrow": "使用条款",
"t.h1": "这份约定，用大白话讲。",
"t.sub": "Pausely 做什么、不承诺什么，Premium 如何计费，以及严格模式对你的要求。",
"t.meta": "自 {DATE} 起生效 · Pausely，由 {COMPANY} 提供",

"t.acceptance.h": "1. 条款的接受",
"t.acceptance.b": """
<p>本使用条款（“本条款”）是你与 iPhone 和 iPad 版 Pausely App（“Pausely”或“本 App”）的发行方 {COMPANY}（“我们”）之间的约定。安装或使用 Pausely，即表示你接受本条款以及我们的<a href="{BASE}{L}/privacy/">隐私政策</a>。如果你不同意，请不要使用本 App。</p>
""",
"t.who.h": "2. 谁可以使用 Pausely",
"t.who.b": """
<p>使用 Pausely，你必须年满 13 周岁，或达到你所在地区规定的数字同意年龄。Pausely 是你为自己、在自己的设备上安装的工具。它不是家长控制产品，也不得用于管理或监控他人的设备。</p>
""",
"t.what.h": "3. Pausely 是什么——以及不是什么",
"t.what.b": """
<p>Pausely 是一个自我约束的工具：它在你选中的 App 前加上一次暂停，把结果记录在你的设备上，并把你自己的进展呈现给你。它的用意，是把一个自动的习惯变成一次有意识的选择。</p>
<p>Pausely <strong>不是</strong>医疗、心理或治疗服务，其中的任何内容——包括心情记录、日志提示、各种分析，以及 AI 反思写回来的任何文字——都不构成建议、诊断或治疗。如果你正被强迫性使用、焦虑、抑郁，或任何影响你身心状态的事情困扰，请与有资质的专业人士谈一谈。紧急情况下，请拨打当地的紧急电话。</p>
<p>Pausely 同样<strong>不是安全产品，也不是家长控制产品</strong>。它被设计成恰好如你所要求的那么强：App 可以删除，“屏幕使用时间”权限可以在 iOS 设置中收回，而遮挡只在 App 处于已安装且已获授权的状态时存在。</p>
""",
"t.screentime.h": "4. “屏幕使用时间”、严格模式与你的承诺",
"t.screentime.b": """
<p>Pausely 依赖 Apple 的“屏幕使用时间”框架。执行遮挡的是 Apple，Pausely 只是提出请求。遮挡是否出现、出现得多快，以及能否在重启和 iOS 更新之后延续，最终取决于 iOS，我们无法在所有情形下作出保证。</p>
<p><strong>严格模式</strong>是你与自己立下的承诺。它运行期间，在你选定的时长内，保护无法关闭、规则无法删除、数据无法重置——<em>你不行，我们也不行</em>。我们无法应请求提前结束一次严格模式。不要开启一次你没准备好守住的严格模式，也不要在一台你可能需要不受限制使用的设备上开启它。删除 App 会结束全部遮挡，见第 3 条。</p>
<p><strong>完全拦截的规则</strong>在其时段内不提供任何通行的余地。同样的提醒适用于它。</p>
""",
"t.data.h": "5. 你的数据与你的设备",
"t.data.b": """
<p>Pausely 记录的一切都保存在你的设备上——唯一的、可选的例外见<a href="{BASE}{L}/privacy/">隐私政策</a>。你的设备、它的密码和它的备份由你负责。如果你删除 App、重置全部数据，或在没有备份的情况下丢失设备，你的规则、日志和历史就没有了，我们这边没有副本可以恢复。你购买的 Premium 是另一回事：它属于你的 Apple 账户，可以在任何登录了该账户的设备上恢复。</p>
<p>你写进 Pausely 的内容属于你。我们对此不主张任何权利，也不会收到其中任何内容，除非你打开 AI 反思——即便如此，被发送的也只是第 6 条和隐私政策所描述的那些。</p>
""",
"t.ai.h": "6. AI 反思",
"t.ai.b": """
<p>AI 反思是一个<strong>可选的</strong> Premium 功能，<strong>在你打开它之前一直关着</strong>。打开之后，你在那一次暂停里打下的文字会被发送到我们的服务器，再送到生成回应的 Google。发送什么、永远不发送什么，以及任何内容会被保留多久，都写在<a href="{BASE}{L}/privacy/#ai">隐私政策</a>里，并在 App 内的{K_settings} → {K_ai_reflection} → {K_what_is_sent}中逐条列出。</p>
<p>返回的是<strong>生成的文字</strong>。它可能是错的、没有帮助的，或者不是你所期待的，并且<strong>不构成任何形式的建议</strong>——见第 3 条。不要在其中输入你不希望被第三方处理的内容，也不要在任何要紧的决定上依赖它。我们不保证该功能的可用性、响应速度或持续提供，并可能更换其背后的模型、限制其使用，或将其撤下，而这不影响 App 的其余部分。</p>
<p>你同意不使用该功能生成违法、辱骂或侵权的内容，也不试图套取底层模型或其指令。关闭该功能会让这一切停止，并使 App 回到完全不发起任何网络请求的状态。</p>
""",
"t.subscriptions.h": "7. Premium、订阅与计费",
"t.subscriptions.b": """
<p>Pausely 免费下载、免费使用。<strong>Pausely Premium</strong> 解锁额外功能，以三种形式出售，价格以 App 内和你所在国家/地区 App Store 的显示为准：</p>
<ul>
  <li><strong>Premium 按月</strong>——自动续期订阅，按月计费。</li>
  <li><strong>Premium 按年</strong>——自动续期订阅，按年计费；在提供试用的地区，以<strong>免费试用</strong>开始。</li>
  <li><strong>Premium 永久</strong>——一次性购买，不会续期。</li>
</ul>
<p>确认购买时，费用将记入你的 Apple 账户。除非在试用结束前至少 24 小时取消，免费试用会转为付费订阅。除非在当前周期结束前至少 24 小时关闭自动续期，订阅将按相同价格和相同周期自动续期；续期费用会在该周期结束前 24 小时内扣取。你可以在<a href="https://apps.apple.com/account/subscriptions">App Store 订阅设置</a>中管理或取消订阅；取消于当前周期结束时生效，已过周期中未使用的部分不作按比例退款。退款由 Apple 依其政策处理。在新设备上找回 Premium，请使用 App 内的{K_restore}。</p>
<p><strong>如果订阅到期</strong>，你已经设好的东西一样都不会被移除：每条规则照常运行，也仍然可以编辑，你选的那种暂停也照常工作。关上的只是继续添加更多 Premium 内容这件事。Premium 所包含的功能可能随时间变化；我们不会在没有事先告知的情况下，从一份有效订阅中移除某项功能。</p>
""",
"t.licence.h": "8. 许可与知识产权",
"t.licence.b": """
<p>在遵守本条款和 App Store 使用规则的前提下，我们授予你一项个人的、非独占的、不可转让的、可撤销的许可，允许你在自己拥有或控制的 iPhone 或 iPad 上安装并使用 Pausely。Pausely 及其名称、设计、插图、文字与代码归 {COMPANY} 所有，受著作权法及其他法律保护。除法律明确允许的情形外，你不得复制、修改、分发、销售、出租、反向工程本 App，或据以创作衍生作品。</p>
""",
"t.use.h": "9. 可接受的使用",
"t.use.b": """
<p>你同意不以任何违法的方式使用 Pausely，不干扰本 App 或 Apple 的服务，不试图绕开 App Store 的购买机制，也不将其安装在你无权管理的设备上。你同意不用它在未取得他人知情同意的情况下限制或监控他人。</p>
""",
"t.termination.h": "10. 终止",
"t.termination.b": """
<p>你可以随时通过删除 Pausely 来停止使用它。若你违反本条款，我们可以中止或终止你的许可。第 5、6、8、11、12 和 14 条在终止后继续有效。删除 App 并不会取消一份有效的订阅——请在你的 App Store 设置中取消。</p>
""",
"t.warranty.h": "11. 保证与责任",
"t.warranty.b": """
<p>Pausely 按“现状”和“现有可用”提供，不作任何明示或默示的保证，包括不保证它会在任何情形下都拦住某个 App、不保证运行不中断或无差错、不保证 AI 反思写出的任何内容准确或有用，也不保证它会改变你的习惯。在法律允许的最大范围内，{COMPANY} 不对因你使用或无法使用本 App 而产生的任何间接、附带、特殊、后果性或惩罚性损害，或任何数据丢失承担责任——包括某次遮挡出现或未出现的后果、你自己选择开启的一次严格模式的后果，或 AI 反思所产出内容的后果。在责任无法排除的情形下，其上限为你在提出主张之前十二个月内为 Premium 向我们支付的金额。本条款中的任何内容，都不限制你作为消费者所享有的、不可放弃的权利。</p>
""",
"t.apple.h": "12. 关于 Apple",
"t.apple.b": """
<p>Pausely 通过 Apple App Store 分发。本条款是你与 {COMPANY} 之间的约定，与 Apple 无关。Apple 没有义务为本 App 提供维护或支持，也不负责处理与本 App 有关的任何主张，包括产品责任、法律合规或知识产权方面的主张。Apple 及其子公司是本条款的第三方受益人，可向你主张本条款。本条款未作规定之处，适用 Apple 的<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">授权应用程序最终用户许可协议</a>。你声明你不身处受美国政府禁运的国家，也未被列为受禁方，并且在使用本 App 时须遵守任何适用的第三方条款。</p>
""",
"t.changes.h": "13. 本条款的变更",
"t.changes.b": """
<p>我们可能不时更新本条款。更新时顶部的日期会随之变动，重要变更会写进 App 的版本说明。更新之后继续使用，即表示你接受修订后的条款。</p>
""",
"t.law.h": "14. 适用法律",
"t.law.b": """
<p>本条款受 {COMPANY} 经营所在地巴基斯坦的法律管辖，不考虑其法律冲突规则。若你居住国的法律赋予你不可通过合同排除的保护，则以该等保护为准。</p>
""",
"t.contact.h": "15. 联系我们",
"t.contact.b": """
<p>关于本条款的问题请联系：{MAIL}。</p>
""",

"d.eyebrow": "你的数据",
"d.h1": "删除你的数据",
"d.sub": "Pausely 知道的一切都在你的设备上。这里说明怎样抹掉它、订阅会怎样，以及我们这边还留下什么——什么都没有。",
"d.meta": '另见<a href="{BASE}{L}/privacy/">隐私政策</a>',

"d.where.h": "什么存在哪里",
"d.where.b": """
<p class="lead">Pausely 没有账号，它的服务器也不为任何人留档。它拥有的一切都在你的设备上，你不必问我们就能抹掉。</p>
<div class="table-wrap"><table>
<tr><th>数据</th><th>存放在哪里</th><th>怎样移除</th></tr>
<tr><td>规则、暂停历史、连续记录、日志、心情记录、替代选项、设置</td><td>你设备上属于 App 的私有存储</td><td>{RESET}，或删除 App</td></tr>
<tr><td>你选中的 App</td><td>App 私有存储中不透明的“屏幕使用时间”令牌</td><td>同上；在 iOS 设置中收回“屏幕使用时间”权限，也会结束全部遮挡</td></tr>
<tr><td>小组件快照</td><td>你设备上一个只含计数与日期的小文件</td><td>随重置一起移除，也随 App 一起移除</td></tr>
<tr><td>Premium 权益</td><td>你的 Apple 账户（Apple 侧），以及其状态在你设备上的一份副本</td><td>在你的 App Store 设置中管理——见下文</td></tr>
<tr><td>你在一次 AI 反思中打下的内容</td><td>被回答之后哪里都没有。我们的服务器既不保存提问也不保存回答；Google 会把输入和输出保留最多 24 小时</td><td>没有可删的东西。在{K_settings} → {K_ai_reflection}中关闭该功能，此后就不会再发送任何内容</td></tr>
<tr><td>账号、个人资料，或任何带着你名字的东西</td><td>—</td><td>并不存在。我们从来就没有可删的。</td></tr>
</table></div>
""",
"d.inapp.h": "在 App 里抹掉",
"d.inapp.b": """
<ol class="steps">
  <li><div>打开 Pausely，进入{K_settings}。</div></li>
  <li><div>点按{K_your_data}，再点按{K_reset_all}。</div></li>
  <li><div>确认。每一次暂停、每一次成功、每条规则、每篇日志和每次心情记录都会被抹掉，遮挡撤下，时间表收回，App 从设置重新开始。</div></li>
</ol>
<div class="callout warm"><span class="tile">{lock}</span><div><strong>严格模式运行时它会拒绝执行。</strong>那是你请这个 App 替你守住的唯一一个承诺。等到你选定的时刻、那一段结束之后，再来重置。</div></div>
""",
"d.uninstall.h": "删除 App",
"d.uninstall.b": """
<p>把 Pausely 从设备上删除，会连同它的全部数据（包括“屏幕使用时间”令牌）一起带走，并立刻结束全部遮挡。如果这个 App 被包含在 iCloud 备份或加密的本地备份里，那份副本属于你的 Apple 账户，受 Apple 的条款约束；我们无法访问它。</p>
""",
"d.subscription.h": "你的订阅",
"d.subscription.b": """
<p>重置数据和删除 App 都不会取消订阅——它属于你的 Apple 账户，而不是这个 App。请在 <a href="https://apps.apple.com/account/subscriptions">App Store 订阅设置</a>中取消；在当前周期结束之前它仍然有效。退款由 <a href="https://support.apple.com/billing">Apple 支持</a>处理。永久购买不会续期，也没有什么需要取消。</p>
""",
"d.email.h": "问问我们",
"d.email.b": """
<p>如果你想要一份书面确认，说明我们没有任何关于你的信息，或者你认为我们有，请从任意邮箱写信到 {MAIL}。我们会在 30 天内回复。请不要把你的日志、心情记录或它们的截图发给我们——回答你的问题并不需要它们。</p>
""",

"nf.eyebrow": "404",
"nf.h1": "这里没什么可看的。",
"nf.sub": "而这一次，这并不是本意。",
"nf.cta": "回到帮助",
"nf.b": '这个页面不在这里。试试<a href="{BASE}/">帮助</a>、<a href="{BASE}/privacy/">隐私政策</a>或<a href="{BASE}/terms/">使用条款</a>。',

}

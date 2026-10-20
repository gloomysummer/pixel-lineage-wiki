// ============================================================
// [Config 层] site.config.ts — 站点唯一真相源
//
// 起一个新站时，这是你唯一必须改的代码文件。
// 上游模板升级只会动 Code 层，与本文件的冲突是预期内的、
// 且永远保留你自己的值（见 docs/CONTENT-LAYERS.md）。
//
// 规则：所有派生值（JSON-LD、canonical、hreflang、sitemap、
// 收录提交）都从这里读，禁止在页面里硬编码域名。
// ============================================================

export const siteConfig = {
  /** 游戏官方名（用于 title/keywords/JSON-LD） */
  gameName: "Pixel Lineage",
  /** 站点品牌名（og:site_name、页脚、品牌后缀） */
  siteName: "Pixel Lineage Wiki",
  /** 站点根 URL，结尾不带斜杠 */
  siteUrl: "https://pixel-lineage.quest",
  /** 品牌后缀（SERP title 用，严格 ≤12 字符，含 | 与空格） */
  titleSuffix: " | PL Wiki",
  /** 站点默认语言（URL 无前缀）；其余语言加前缀，缺失内容回退默认语言 */
  defaultLocale: "en",
  /** 实际存在翻译内容的语言（双轨 hreflang：只为物理存在的翻译输出 alternate） */
  locales: ["en"],
  /** 站长联系邮箱（法律合规三件套用） */
  contactEmail: "contact@pixel-lineage.quest",
  /** 广告与统计（全部默认关闭——env/config 门控，模板升级不会自动开启） */
  ads: {
    adsenseClient: "", // 例: "ca-pub-XXXXXXXXXXXXXXXX"，留空 = 不渲染广告位
    gaMeasurementId: "G-2QYE09XE85", // GA4 Measurement ID
  },
  /**
   * Adsterra 变现（可选，默认关闭）。
   */
  adsterra: {
    enabled: true,
    /**
     * 每种尺寸一个独立 Zone（Adsterra 对同页同 key 只计一次展示）。
     * key 必须是 32 位小写 hex，否则 AdSlot 的占位符防御会让整槽不渲染。
     * 两处必须一致：这里 + public/ads/banner-<size>.html 里的 atOptions.key。
     *
     * 后台 placement（pixel-lineage.quest · domain_id 6136749）：
     *   160x300_1  31828711    160x600_1  31828714
     *   300x250_1  31828715    320x50_1   31828712
     *   468x60_1   31828710    728x90_1   31828713
     * 后台没有 Popunder / SocialBar / NativeBanner —— 符合"弹窗类永久关闭"的既定策略。
     */
    banners: {
      "banner-468x60": { key: "1e7c4f6780af91eba5543d5562c33b74", width: 468, height: 60, enabled: true },
      "banner-160x300": { key: "b7b59f059275fd8dccb04bb9f334c18e", width: 160, height: 300, enabled: true },
      "banner-320x50": { key: "b7e7350fc7e76152d6775e689b8011d0", width: 320, height: 50, enabled: true },
      "banner-728x90": { key: "18d40b692ecc5a1fd30b02e7de20301d", width: 728, height: 90, enabled: true },
      "banner-160x600": { key: "f2f35f0d06b8d766feb7ea42aabcd961", width: 160, height: 600, enabled: true },
      "banner-300x250": { key: "b3e29629ce246f3970006b69e454d496", width: 300, height: 250, enabled: true },
    },
  },
  /** 搜索引擎站长验权 */
  verification: {
    googleSiteVerification: "7JjfXMCr0T2QUqU6YYLEbID_BQzGP0kl_rR7zBkvSjA",
  },
  /** 收录提交（可选） */
  indexing: {
    indexNowKey: "f11976fd1fae469097f9a3fa56f3caa0",
  },
  /** 官方社区与实体链接（用于 Schema.org Organization sameAs 知识图谱绑定，留空不输出） */
  officialLinks: {
    roblox: "https://www.roblox.com/games/126256942507957/Pixel-Lineage",
    discord: "",
    twitter: "",
    youtube: "",
    steam: "",
    officialSite: "",
  },
} as const;

export type SiteConfig = typeof siteConfig;

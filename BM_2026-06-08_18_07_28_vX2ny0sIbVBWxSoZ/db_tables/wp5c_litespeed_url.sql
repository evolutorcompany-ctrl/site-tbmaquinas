/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_litespeed_url`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_litespeed_url`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_litespeed_url` ( `id` bigint NOT NULL AUTO_INCREMENT, `url` varchar(500) COLLATE utf8mb4_unicode_520_ci NOT NULL, `cache_tags` varchar(1000) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', PRIMARY KEY (`id`), UNIQUE KEY `url` (`url`(191)), KEY `cache_tags` (`cache_tags`(191))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

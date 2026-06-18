/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp_terms`; */
/* PRE_TABLE_NAME: `1780942049_wp_terms`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp_terms` ( `term_id` bigint unsigned NOT NULL AUTO_INCREMENT, `name` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', `slug` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', `term_group` bigint NOT NULL DEFAULT '0', PRIMARY KEY (`term_id`), KEY `slug` (`slug`(191)), KEY `name` (`name`(191))) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp_terms` (`term_id`, `name`, `slug`, `term_group`) VALUES (1,'Uncategorized','uncategorized',0);

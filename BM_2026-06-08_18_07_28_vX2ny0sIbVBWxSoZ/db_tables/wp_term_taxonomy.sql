/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp_term_taxonomy`; */
/* PRE_TABLE_NAME: `1780942049_wp_term_taxonomy`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp_term_taxonomy` ( `term_taxonomy_id` bigint unsigned NOT NULL AUTO_INCREMENT, `term_id` bigint unsigned NOT NULL DEFAULT '0', `taxonomy` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', `description` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL, `parent` bigint unsigned NOT NULL DEFAULT '0', `count` bigint NOT NULL DEFAULT '0', PRIMARY KEY (`term_taxonomy_id`), UNIQUE KEY `term_id_taxonomy` (`term_id`,`taxonomy`), KEY `taxonomy` (`taxonomy`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (1,1,'category','',0,1);

/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_litespeed_url_file`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_litespeed_url_file`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_litespeed_url_file` ( `id` bigint NOT NULL AUTO_INCREMENT, `url_id` bigint NOT NULL, `vary` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT 'md5 of final vary', `filename` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT 'md5 of file content', `type` tinyint NOT NULL COMMENT 'css=1,js=2,ccss=3,ucss=4', `mobile` tinyint NOT NULL COMMENT 'mobile=1', `webp` tinyint NOT NULL COMMENT 'webp=1', `expired` int NOT NULL DEFAULT '0', PRIMARY KEY (`id`), KEY `filename` (`filename`), KEY `type` (`type`), KEY `url_id_2` (`url_id`,`vary`,`type`), KEY `filename_2` (`filename`,`expired`), KEY `url_id` (`url_id`,`expired`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

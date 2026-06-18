/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_yoast_indexable_hierarchy`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_yoast_indexable_hierarchy`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_yoast_indexable_hierarchy` ( `indexable_id` int unsigned NOT NULL, `ancestor_id` int unsigned NOT NULL, `depth` int unsigned DEFAULT NULL, `blog_id` bigint NOT NULL DEFAULT '1', PRIMARY KEY (`indexable_id`,`ancestor_id`), KEY `indexable_id` (`indexable_id`), KEY `ancestor_id` (`ancestor_id`), KEY `depth` (`depth`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_yoast_indexable_hierarchy` (`indexable_id`, `ancestor_id`, `depth`, `blog_id`) VALUES (65,0,0,1),(66,0,0,1),(67,0,0,1),(68,0,0,1),(69,0,0,1),(70,0,0,1),(71,0,0,1),(72,0,0,1),(73,0,0,1),(74,0,0,1),(75,0,0,1),(76,0,0,1),(77,0,0,1),(78,0,0,1),(79,0,0,1),(80,0,0,1),(87,0,0,1),(88,0,0,1),(89,0,0,1),(90,0,0,1),(91,0,0,1),(94,0,0,1);

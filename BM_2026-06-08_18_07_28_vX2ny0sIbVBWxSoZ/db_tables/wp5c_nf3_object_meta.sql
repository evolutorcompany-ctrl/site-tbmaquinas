/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_nf3_object_meta`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_nf3_object_meta`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_nf3_object_meta` ( `id` int NOT NULL AUTO_INCREMENT, `parent_id` int NOT NULL, `key` longtext NOT NULL, `value` longtext, `meta_key` longtext, `meta_value` longtext, UNIQUE KEY `id` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

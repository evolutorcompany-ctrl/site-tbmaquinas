/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_nf3_relationships`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_nf3_relationships`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_nf3_relationships` ( `id` int NOT NULL AUTO_INCREMENT, `child_id` int NOT NULL, `child_type` longtext NOT NULL, `parent_id` int NOT NULL, `parent_type` longtext NOT NULL, `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, `updated_at` datetime DEFAULT NULL, UNIQUE KEY `id` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

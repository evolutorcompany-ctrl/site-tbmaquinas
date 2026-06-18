/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_nf3_objects`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_nf3_objects`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_nf3_objects` ( `id` int NOT NULL AUTO_INCREMENT, `type` longtext, `title` longtext, `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, `updated_at` datetime DEFAULT NULL, `object_title` longtext, UNIQUE KEY `id` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

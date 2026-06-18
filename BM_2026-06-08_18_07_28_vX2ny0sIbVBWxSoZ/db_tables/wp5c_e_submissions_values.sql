/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_e_submissions_values`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_e_submissions_values`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_e_submissions_values` ( `id` bigint unsigned NOT NULL AUTO_INCREMENT, `submission_id` bigint unsigned NOT NULL DEFAULT '0', `key` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, PRIMARY KEY (`id`), KEY `submission_id_index` (`submission_id`), KEY `key_index` (`key`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

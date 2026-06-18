/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_nf3_forms`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_nf3_forms`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_nf3_forms` ( `id` int NOT NULL AUTO_INCREMENT, `title` longtext, `key` longtext, `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, `updated_at` datetime DEFAULT NULL, `views` int DEFAULT NULL, `subs` int DEFAULT NULL, `form_title` longtext, `default_label_pos` varchar(15) DEFAULT NULL, `show_title` bit(1) DEFAULT NULL, `clear_complete` bit(1) DEFAULT NULL, `hide_complete` bit(1) DEFAULT NULL, `logged_in` bit(1) DEFAULT NULL, `seq_num` int DEFAULT NULL, UNIQUE KEY `id` (`id`)) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `1780942049_wp5c_nf3_forms` (`id`, `title`, `key`, `created_at`, `updated_at`, `views`, `subs`, `form_title`, `default_label_pos`, `show_title`, `clear_complete`, `hide_complete`, `logged_in`, `seq_num`) VALUES (2,'Contato',NULL,'2023-10-22 18:13:06','2023-10-22 21:13:06',NULL,NULL,'Contato','above',1,1,1,0,NULL);

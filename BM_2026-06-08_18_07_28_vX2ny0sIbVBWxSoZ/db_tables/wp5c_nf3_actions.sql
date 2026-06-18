/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_nf3_actions`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_nf3_actions`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_nf3_actions` ( `id` int NOT NULL AUTO_INCREMENT, `title` longtext, `key` longtext, `type` longtext, `active` tinyint(1) DEFAULT '1', `parent_id` int NOT NULL, `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, `updated_at` datetime DEFAULT NULL, `label` longtext, UNIQUE KEY `id` (`id`)) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `1780942049_wp5c_nf3_actions` (`id`, `title`, `key`, `type`, `active`, `parent_id`, `created_at`, `updated_at`, `label`) VALUES (5,NULL,NULL,'successmessage',1,2,'2023-10-22 18:13:06','2023-10-22 21:13:06','Mensagem de Sucesso'),(6,NULL,NULL,'email',1,2,'2023-10-22 18:13:06','2023-10-22 21:13:06','E-mail do administrador'),(7,NULL,NULL,'save',1,2,'2023-10-22 18:13:06','2023-10-22 21:13:06','Record Submission');

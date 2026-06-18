/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_cm_popfly_history`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_cm_popfly_history`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_cm_popfly_history` ( `event_id` bigint NOT NULL AUTO_INCREMENT, `event_type` enum('cl','im') NOT NULL, `campaign_id` bigint DEFAULT NULL, `amount` int DEFAULT '1', `banner_id` varchar(32) DEFAULT NULL, `referer_url` varchar(150) NOT NULL, `remote_ip` varchar(20) NOT NULL, `webpage_url` varchar(200) NOT NULL, `remote_country` varchar(20) NOT NULL, `remote_city` varchar(30) NOT NULL DEFAULT '', `regdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (`event_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

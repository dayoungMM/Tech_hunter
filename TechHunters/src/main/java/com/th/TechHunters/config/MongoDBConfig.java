package com.th.TechHunters.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@Configuration
@EnableMongoRepositories(basePackages = "com.th.TechHunters.repository")
public class MongoDBConfig {

}

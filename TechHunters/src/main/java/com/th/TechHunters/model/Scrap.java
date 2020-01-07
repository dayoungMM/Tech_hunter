package com.th.TechHunters.model;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;
import lombok.Setter;


@Document("scrap_db")
@Getter
@Setter
public class Scrap {
	
	@Id
	private ObjectId _id;
	private User user;
	
	private String img;
	private String title;
	private String preview;
}
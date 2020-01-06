package com.th.TechHunters.repository;


import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import com.th.TechHunters.model.News;

@Repository
public interface NewsMongoDBRepository extends MongoRepository<News, Long> {
	
	public List<News> findByImgAndTitleAndLink(String img, String title, String link);
	
//	List<News> findByImg(String img);
//	List<News> findByTitle(String title);
//	List<News> findByLink(String link);
}





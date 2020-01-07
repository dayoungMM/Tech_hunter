package com.th.TechHunters.repository;


import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import com.th.TechHunters.model.News;
import com.th.TechHunters.model.Scrap;

@Repository
public interface ScrapMongoDBRepository extends MongoRepository<Scrap, Long> {
	
	public List<Scrap> findByImgAndTitleAndPreview(String img, String title, String preview);
	
//	List<News> findByImg(String img);
//	List<News> findByTitle(String title);
//	List<News> findByLink(String link);
}





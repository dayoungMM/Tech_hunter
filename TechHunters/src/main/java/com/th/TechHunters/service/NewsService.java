package com.th.TechHunters.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.th.TechHunters.model.News;
import com.th.TechHunters.repository.NewsMongoDBRepository;

@Service
public class NewsService {
	@Autowired
	private NewsMongoDBRepository NewsMongoDBRepository;

	public List<News> getImgAndTitleAndLink(String img, String title, String link) {
		return NewsMongoDBRepository.findByImgAndTitleAndLink(img, title, link);
	}

	public List<News> getList() {
		return NewsMongoDBRepository.findAll();
	}
	
}

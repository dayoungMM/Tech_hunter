package com.th.TechHunters.controller;

import java.util.List;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.th.TechHunters.model.News;
import com.th.TechHunters.repository.NewsMongoDBRepository;
import com.th.TechHunters.service.NewsService;

@Controller
public class NewsControlller {
	
	@Autowired
	NewsService newsService;

	@Autowired
	private NewsMongoDBRepository NewsMongoDBRepository;

	@Autowired
	HttpSession session;

	@GetMapping({ "/ainews" })
	public String ainews() {
		return "ainews";
	}

	@PostMapping("/ainews")
	public String signinPost(@ModelAttribute News news) {
		News dbnews = (News) newsService.getImgAndTitleAndLink(news.getImg(), news.getTitle(),
				news.getLink());
		if (dbnews != null) {
			session.setAttribute("news_info", dbnews);
			System.out.println(dbnews);
		}
		return "dbnews";
	}
	
	@GetMapping({ "/bigdatanews" })
	public String bigdatanews() {
		return "bigdatanews";
	}
	
	@GetMapping({ "/etcnews" })
	public String etcnews() {
		return "etcnews";
	}

	@GetMapping({ "/list" })
	@ResponseBody
	public List<News> list() {
//		List<News> list = newsService.getList();
		List<News> list = NewsMongoDBRepository.findAll();
		return list;
	}
}
package com.th.TechHunters.controller;

import java.util.List;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.th.TechHunters.model.Scrap;
import com.th.TechHunters.model.User;
import com.th.TechHunters.repository.ScrapMongoDBRepository;


@Controller
public class ScrapController {


	@Autowired
	private ScrapMongoDBRepository ScrapMongoDBRepository;
	
	@Autowired
	HttpSession session;

	@GetMapping({ "/ainews" })
	public String ainews() {
		return "ainews";
	}


	@PostMapping("/ainews")
	public String ainewsPost(@ModelAttribute Scrap scrap) {
		ScrapMongoDBRepository.save(scrap);
		
		return "redirect:/";
	}
	
}
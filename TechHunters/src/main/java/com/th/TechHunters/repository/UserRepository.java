package com.th.TechHunters.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.th.TechHunters.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
	public User findByEmailAndPwd(String email, String pwd);
}

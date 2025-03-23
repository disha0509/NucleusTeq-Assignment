package com.example.demo.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.model.HR;

@Repository
public interface HRRepository extends JpaRepository<HR, Long> {
    Optional<HR> findByUsername(String username);
}

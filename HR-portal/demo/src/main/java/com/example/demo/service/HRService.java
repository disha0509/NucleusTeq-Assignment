package com.example.demo.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.model.HR;
import com.example.demo.repository.HRRepository;

@Service
public class HRService {

    @Autowired
    private HRRepository hrRepository;

    // Authenticate HR
    public boolean authenticate(String username, String password) {
        Optional<HR> hr = hrRepository.findByUsername(username);
        return hr.isPresent() && hr.get().getPassword().equals(password);
    }

    // Add HR (only for first-time setup)
    public HR addHR(HR hr) {
        return hrRepository.save(hr);
    }
}

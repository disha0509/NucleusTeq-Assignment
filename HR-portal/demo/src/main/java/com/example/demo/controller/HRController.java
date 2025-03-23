package com.example.demo.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.service.HRService;

@RestController
@RequestMapping("/api/hr")
@CrossOrigin(origins = "http://localhost:5500")  // Allow frontend access
public class HRController {

    @Autowired
    private HRService hrService;

    // Login HR
    @PostMapping("/login")
    public Map<String, String> login(@RequestBody Map<String, String> credentials) {
        String username = credentials.get("username");
        String password = credentials.get("password");

        boolean isValid = hrService.authenticate(username, password);

        Map<String, String> response = new HashMap<>();
        response.put("status", isValid ? "success" : "failed");

        return response;
    }
}

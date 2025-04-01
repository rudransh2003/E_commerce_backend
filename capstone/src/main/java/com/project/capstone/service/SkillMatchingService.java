package com.project.capstone.service;

import com.project.capstone.models.Employee;
import com.project.capstone.models.Project;
import com.project.capstone.repository.EmployeeRepository;
import com.project.capstone.repository.ProjectRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class SkillMatchingService {
    @Autowired
    private EmployeeRepository employeeRepository;

    @Autowired
    private ProjectRepository projectRepository;

    public List<Employee> findMatchingEmployees(Long projectId) 
    {
        Project project = projectRepository.findById(projectId)
                .orElseThrow(() -> new RuntimeException("Project not found"));

        List<Employee> employees = employeeRepository.findAll();

        return employees.stream()
                .filter(emp -> matchesSkills(emp.getSkills(), project.getRequiredSkills()))
                .collect(Collectors.toList());
    }

    private boolean matchesSkills(String employeeSkills,String projectSkills)
    {
        String[] empSkillsArray=employeeSkills.toLowerCase().split(", ");
        String[] projSkillsArray=projectSkills.toLowerCase().split(", ");
        for(String skill:projSkillsArray)
        {
            if(List.of(empSkillsArray).contains(skill))
            {
                System.out.println("Match Found"+ skill);
                return true;
            }
        }
        return false;
    }
    
}

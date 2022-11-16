package edu.upenn.cit594.datamanagement;

import java.util.List;

import edu.upenn.cit594.data.Violation;

public interface violationReader {
	

	//returns complete violation list
	public List<Violation> getAllViolation();

}

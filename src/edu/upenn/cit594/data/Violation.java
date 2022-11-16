package edu.upenn.cit594.data;

import java.util.Date;

public class Violation {
	
	private Date date;
	private int fine;
	private String description;
	private int vehicleId;
	private String state;
	private int violationId;
	private int zip;
	
	public Violation(Date date, int fine, String description, int vehicleId, String state, int violationId, int zip) {
		this.date = date;
		this.fine= fine;
		this.description = description;
		this.vehicleId = vehicleId;
		this.state = state;
		this.violationId = violationId;
		this.zip = zip;

	}

	public Date getDate() {
		return date;
	}

	public String getDescription() {
		return description;
	}

	public int getVehicleId() {
		return vehicleId;
	}

	public String getState() {
		return state;
	}

	public int getViolationId() {
		return violationId;
	}

	public int getFine() {
		return fine;
	}

	public int getZip() {
		return zip;
	}
	
	

}

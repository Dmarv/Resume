package edu.upenn.cit594.datamanagement;

import edu.upenn.cit594.data.Violation;
import edu.upenn.cit594.logging.Logger;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * 
 * @author Daniel
 *
 */

public class CsvViolationReader implements violationReader {

	protected List<Violation> violationsList;
	protected String filename; 
	protected String logFileName;

	public CsvViolationReader(String filename , String logFileName) {
		this.filename = filename;
		violationsList = populateViolationList();
		this.logFileName = logFileName;
		
	}


	private List<Violation> populateViolationList() {

		List<Violation> violations = new ArrayList<Violation>();
		
		//create file object
		File file = new File(filename);

		try {

			// make file, check for existence, readable and then open.
			@SuppressWarnings("resource")
			BufferedReader br = new BufferedReader(new FileReader(file));
			Logger l = Logger.getInstance(logFileName);
			l.log(String.valueOf(System.currentTimeMillis()) + " " + this.filename );

			String line = "";

			/*
			 * while there is another line, read it and store it in a list
			 */
			while (true) {

				try {
					if ((line = br.readLine()) == null)
						break;

				} catch (Exception e) {
					System.out.println("Error");
					e.printStackTrace();
				}

				Violation violation = formatViolation(line);

				violations.add(violation);

			}

		} catch (Exception e) {
			System.out.println("Error");
			e.printStackTrace();
		}
		return violations;
	}


	private Violation formatViolation(Object object) {
		String line = (String) object;
		Date date = null;
		int fine = -1;
		String description = "";
		int vehicleId = -1;
		String state = "";
		int violationId = -1;
		int zip = -1;

		// split up data by comma and prase data
		String[] data = line.split(",");

		// format our date correctly
		SimpleDateFormat format = new SimpleDateFormat("YYYY-MM-DD'T'hh:mm:ss'Z'");
		try {
			date = format.parse(data[0]);
		} catch (ParseException e) {
			e.printStackTrace();
		}

		fine = Integer.parseInt(data[1]);
		description = data[2];
		vehicleId = Integer.parseInt(data[3]);
		state = data[4];
		violationId = Integer.parseInt(data[5]);
		// check if there is zipcode, if so, store it. stores as -1 is not data
		if (data.length == 7) {
			zip = Integer.parseInt(data[6]);
		}

		Violation violation = new Violation(date, fine, description, vehicleId, state, violationId, zip);
		return violation;
	}

	@Override
	public List<Violation> getAllViolation() {
		return violationsList;
	}

//	public static void main(String[] args) {
//
//		CsvViolationReader c = new CsvViolationReader("parking.csv");
//
//		List<Violation> violation = c.getAllViolation();
//
//		for (Violation v : violation) {
//			System.out.println("Date: " + v.getDate() + " Fine: " + v.getFine() + " description: " + v.getDescription()
//					+ " vehicleId: " + v.getVehicleId() + " State: " + v.getState() +  "violationId: " + v.getViolationId()
//					+ "Zip: " + v.getZip());
//		}
//	}
//	
	

}

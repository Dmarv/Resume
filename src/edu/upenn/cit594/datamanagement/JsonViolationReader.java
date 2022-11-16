package edu.upenn.cit594.datamanagement;

import java.io.File;
import java.io.FileReader;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import edu.upenn.cit594.data.Violation;
import edu.upenn.cit594.logging.Logger;

/**
 * 
 * @author Daniel
 *
 */

public class JsonViolationReader implements violationReader {

	protected List<Violation> violationsList;
	protected String filename; 
	protected String logFileName;

	public JsonViolationReader(String filename , String logFileName) {
		this.filename= filename; 
		violationsList = populateViolationList();
		this.logFileName = logFileName;
	}

	
	private List<Violation> populateViolationList() {

		List<Violation> violations = new ArrayList<Violation>();
		
		//create file object
		File file = new File(filename);

		try {

			JSONParser parser = new JSONParser();

			// parse and add to list
			JSONArray jsonViolations = (JSONArray) parser.parse(new FileReader(file));
			
			Logger l = Logger.getInstance(logFileName);
			l.log(String.valueOf(System.currentTimeMillis()) + " " + this.filename );

			@SuppressWarnings("rawtypes")
			Iterator iter = jsonViolations.iterator();

			while (iter.hasNext()) {
				JSONObject jsonViolation = (JSONObject) iter.next();

				// call helper function to format jsonObject as a violation
				Violation violation = formatViolation(jsonViolation);

				violations.add(violation);
			}

		} catch (Exception e) {
			System.out.println("Error");
			e.printStackTrace();
		}
		return violations;

	}

	/**
	 * helper function that takes in one line and formats and stores one Violation
	 * Object
	 */


	private Violation formatViolation(Object object) {

		JSONObject jsonViolation = (JSONObject) object;
		Date date = null;
		int fine = -1;
		String description = "";
		int vehicleId = -1;
		String state = "";
		int violationId = -1;
		int zip = -1;

		// get the strings of the data we found
		String dateString = jsonViolation.get("date").toString();
		String fineString = jsonViolation.get("fine").toString();
		description = jsonViolation.get("violation").toString();
		String vehicleIdString = jsonViolation.get("plate_id").toString();
		state = jsonViolation.get("state").toString();
		String violationIdString = jsonViolation.get("ticket_number").toString();
		String zipString = jsonViolation.get("zip_code").toString();

		// format as int
		fine = Integer.parseInt(fineString);
		vehicleId = Integer.parseInt(vehicleIdString);
		violationId = Integer.parseInt(violationIdString);

		// format our date correctly
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
		try {
			date = format.parse(dateString);
		} catch (ParseException e) {
			e.printStackTrace();
		}

		// format zip as int. If missing, store as -1;
		if (zipString.length() > 4) {
			zip = Integer.parseInt(zipString);
		}

		// store as violation and return it
		Violation violation = new Violation(date, fine, description, vehicleId, state, violationId, zip);
		return violation;

	}

	@Override
	public List<Violation> getAllViolation() {

		return violationsList;
	}

//	public static void main(String[] args) {
//
//		JsonViolationReader j = new JsonViolationReader("parking.json");
//
//		List<Violation> violation = j.getAllViolation();
//
//		for (Violation v : violation) {
//			System.out.println("Date: " + v.getDate() + " Fine: " + v.getFine() + " description: " + v.getDescription()
//					+ " vehicleId: " + v.getVehicleId() + " State: " + v.getState() + " violationId: " + v.getViolationId()
//					+ " Zip: " + v.getZip());
//		}
//
//	}
	
	
	

}

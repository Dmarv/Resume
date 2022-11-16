package edu.upenn.cit594.logging;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Logger {

	// use FileWriter class so we can append to a file if it already exists
	private FileWriter out;

	private Logger(String logFileName) {

		try {
			File file = new File(logFileName);
			if (!file.exists()) {
				file.createNewFile();

			}
			out = new FileWriter(file, true);

		} catch (Exception e) {
		}


	}

	// initalize to null so we can set it later

	private static Logger instance = null;

	// will only make a new file once during a program
	public static Logger getInstance(String logFileName) {

		if (instance == null) {
			instance = new Logger(logFileName);
		}

		return instance;
	}

	public void log(String msg) {
		try {
			out.write(msg + "\n");
		} catch (IOException e) {
			e.printStackTrace();
		}
		try {
			out.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void closePrintWriter() throws IOException {
		out.close();

	}

}

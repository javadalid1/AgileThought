package com.zetcode;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
class GetRequest {
	public static void main(String[] args) {
		String url = "http://postman-echo.com/get?test123";
		String respuesta = "";
		try {
			respuesta = peticionHttpGet(url);
			System.out.println("La respuesta es:\n" + respuesta);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static String peticionHttpGet(String urlParaVisitar) throws Exception {
		StringBuilder resultado = new StringBuilder();
		URL url = new URL(urlParaVisitar);

		HttpURLConnection conexion = (HttpURLConnection) url.openConnection();
		conexion.setRequestMethod("GET");
		BufferedReader rd = new BufferedReader(new InputStreamReader(conexion.getInputStream()));
		String linea;
		while ((linea = rd.readLine()) != null) {
			resultado.append(linea);
		}
		rd.close();
		return resultado.toString();
	}
}
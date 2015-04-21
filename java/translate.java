import java.net.*;
import java.util.*;

public class translate {
	
	public static String translate(String to_translate, String to_langage, String from_langage){
		String page, result, hl, sl, q;
		
		String before_trans = "class=\"t0\">";
		
		//String charset = java.nio.charset.StandardCharsets.UTF_8.name();
		String charset = "UTF-8";
		
		try{
			hl = URLEncoder.encode(to_langage, charset);
			sl = URLEncoder.encode(from_langage, charset);
			q = URLEncoder.encode(to_translate, charset);
		}catch(Exception e){
			e.printStackTrace();
			return "";
		}
		
		String query = String.format("https://translate.google.com/m?hl=%s&sl=%s&q=%s", hl,sl,q);
		
		try {
			page = URLConnectionReader.getText(query);
		} catch (Exception e) {
			e.printStackTrace();
			return "";
		}
		result = page.substring(page.indexOf(before_trans)+before_trans.length());
		result = result.split("<")[0];
		return result;
	}
	public static void main(String[] args){
		String text = "Salut toi";
		System.out.println(text+" >> "+translate(text,"en","auto"));//simple example to see if it works
		System.out.println(text+" >> "+translate(text,"es","auto"));
	}
}

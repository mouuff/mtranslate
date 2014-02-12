
public class main {
	public static String translate(String to_translate,String to_langage){
		String page,result;
		String before_trans = "class=\"t0\">";
		try {
			page = URLConnectionReader.getText("http://translate.google.com/m?hl="+to_langage+"&q="+to_translate.replace(" ", "+"));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return "";
		}
		result = page.substring(page.indexOf(before_trans)+before_trans.length());
		result = result.split("<")[0];
		return result;
	}
	public static void main(String[] args){
		System.out.print(translate("Salut toi","en"));
	}
}

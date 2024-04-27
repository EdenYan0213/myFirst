import com.baidu.aip.nlp.AipNlp;
import org.json.JSONObject;

public class Main {
    // 设置APPID/AK/SK
    public static final String APP_ID = "51913195";
    public static final String API_KEY = "ddSXjs9KHiGna3FcTG5ZPEOT";
    public static final String SECRET_KEY = "Y3U9byzXxef1Xa0uyaVpqlGvR8PNEoh7";

    public static void main(String[] args) {
        // 初始化一个AipNlp
        AipNlp client = new AipNlp(APP_ID, API_KEY, SECRET_KEY);

        // 可选：设置网络连接参数
        client.setConnectionTimeoutInMillis(2000);
        client.setSocketTimeoutInMillis(60000);

        // 要分析情绪的文本
        String text = "这个电影真不错";

        // 调用情感分析接口
        JSONObject response = client.sentimentClassify(text, null);

        // 解析返回结果，获取情感倾向值
        int positiveProb = response.getJSONObject("items")
                .getJSONObject(String.valueOf(0)).getInt("positive_prob");
        int negativeProb = response.getJSONObject("items")
                .getJSONObject(String.valueOf(0)).getInt("negative_prob");

        // 根据情感倾向值判断情绪
        if (positiveProb > negativeProb) {
            System.out.println("这句话有积极情绪");
        } else if (positiveProb < negativeProb) {
            System.out.println("这句话有消极情绪");
        } else {
            System.out.println("这句话情绪中立");
        }
    }
}

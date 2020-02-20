/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package datasan;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

/**
 *
 * @author Manoj
 */
public class DataSan
{

    public static void main(String[] args) throws IOException
    {
        Stream<String> lines = Files.lines(new File("../aguah_row.csv").toPath());

        Map<String, List<String>> countMap = new HashMap<>();

        lines.forEach((line) ->
        {
            int index = line.lastIndexOf(",");
            String features = line.substring(0, index);
            String waterusage = line.substring(index + 1);

            List<String> list = countMap.get(features);
            if (list == null)
            {
                list = new ArrayList<>();
                countMap.put(features, list);
            }
            list.add(waterusage);
        });

//        countMap.forEach((k, v) ->
//        {
//            System.out.println(k + "\t" + v);
//        });
        try (PrintWriter pw = new PrintWriter("datasan_1.csv"))
        {

            lines = Files.lines(new File("../aguah_row.csv").toPath());
            lines.forEach((line) ->
            {
                int index = line.lastIndexOf(",");
                String features = line.substring(0, index);
                String waterusage = line.substring(index + 1);

                List<String> list = countMap.get(features);

                if (list.size() == 1)
                {
                    pw.println(line);
                }

            });
        }
    }

}

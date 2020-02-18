import java.io.*;
import java.util.*;

class Unique
{
	public static void main(String []args) throws Exception
	{
		Set<String> set1=new HashSet<>();
		Set<String> set2=new HashSet<>();
		Set<String> set3=new HashSet<>();

		int count=0;

		try(BufferedReader br=new BufferedReader(new FileReader(args[0])))
		{
			String line;
			while((line=br.readLine())!=null)
			{
				count++;
				if(count%100==0) System.out.println(count);
				String []tokens=line.split(",");

				set1.add(tokens[0]);
				set2.add(tokens[1]);
				set3.add(tokens[3]);
			}
		}

		List<String> list1=new ArrayList(set1);
		List<String> list2=new ArrayList(set2);
		List<String> list3=new ArrayList(set3);

		list1.sort(null);
		list2.sort(null);
		list3.sort(null);

		System.out.println(list1);
		System.out.println(list2);
		System.out.println(list3);
	}
}
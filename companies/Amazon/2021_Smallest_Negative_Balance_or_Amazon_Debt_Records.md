[Find Countries with the Largest Deficit](https://aonecode.com/interview-question/FindCountriesWithTheLargestDeficit)

```java

public class Soltution {
    public static List<String> minimumDebtMembers(List<DebtRecord> records) {
        HashMap<String, Integer> debt = new HashMap<>();    // get balance by name, name -> balance
        
        for(DebtRecord record: records) {
            debt.put(record.lender, debt.getOrDefault(record.lender, 0) + record.amount);
            debt.put(record.borrower, debt.getOrDefault(record.borrower, 0) - record.amount);
        }
        
        int min = Collections.min(debt.values());
        List<String> res = new ArrayList<>();
        if(min >= 0) {
            return res;
        }

        for(Map.Entry<String, Integer> entry: debt.entrySet()) {
            if(entry.getValue() == min) {
                res.add(entry.getKey());
            }
        }
        
        Collections.sort(res);
        return res;
    }
}


public class DebtRecord {
    String borrower = "";
    String lender = ""; 
    int amount = 0;
    
    DebtRecord(String b, String l, int a) {
        borrower = b;
        lender = l;
        amount = a;
    }
}
```

Complexity:
1. Time: O(N)

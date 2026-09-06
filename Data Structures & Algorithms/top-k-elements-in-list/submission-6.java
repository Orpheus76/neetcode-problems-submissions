class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 1. Compter les fréquences
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        // 2. Récupérer toutes les clés uniques dans une liste
        List<Integer> list = new ArrayList<>(count.keySet());

        // 3. Trier la liste selon la fréquence de manière décroissante
        // Equivalent de: sorted(..., key=lambda x: count[x], reverse=True)
        list.sort((a,b) -> count.get(b) - count.get(a));

        // 4. Extraire les k premiers éléments dans un tableau int[]
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = list.get(i);
        }

        return res;
    }
}

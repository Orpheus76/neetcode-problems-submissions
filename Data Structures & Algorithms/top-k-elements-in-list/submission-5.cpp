#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        // 1. Compter les occurrences (équivalent du dictionnaire)
        std::unordered_map<int, int> count;
        for (int n : nums) {
            count[n]++;
        }

        // 2. Transférer dans un vecteur de paires pour pouvoir trier
        // pair<nombre, frequence>
        std::vector<std::pair<int, int>> freq_pairs;
        for (const auto& entry : count) {
            freq_pairs.push_back({entry.first, entry.second});
        }

        // 3. Trier selon la fréquence de manière décroissante
        // Équivalent de: sorted(..., key=lambda x: count[x], reverse=True)
        std::sort(freq_pairs.begin(), freq_pairs.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return a.second > b.second; // compare les fréquences
        });

        // 4. Extraire les k premiers éléments
        std::vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(freq_pairs[i].first);
        }

        return res;
    }
};

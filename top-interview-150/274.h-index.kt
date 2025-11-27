class Solution {
    fun hIndex(citations: IntArray): Int {
        citations.sort()
        var answer = 0

        for (i in citations.indices) {
            // [0,1,3,5,6]
            // citations.size - i: number of papers from current position to end
            // citations[i]: citation count of current paper
            // If citations[i] >= citations.size - i, then we have at least
            // (citations.size - i) papers with at least (citations.size - i) citations
            if (citations[i] >= citations.size - i) {
                answer = maxOf(answer, citations.size - i)
            }
        }

        return answer
    }
}


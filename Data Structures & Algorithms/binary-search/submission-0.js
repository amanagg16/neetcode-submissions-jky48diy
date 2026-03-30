class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(arr, target) {
        let low = 0, high = arr.length-1;
        let mid;
        while(low <= high) {
            mid = low + Math.floor((high-low)/2);
            if(arr[mid] === target) return mid;
            if(arr[low] === target) return low;
            if(arr[high] === target) return high;
            else if(arr[mid] > target) high = mid-1;
            else if(arr[mid] < target) low = mid+1;
        }
        return -1;
    }
}

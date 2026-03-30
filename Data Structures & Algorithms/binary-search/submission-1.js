class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    BSR(arr, low, high, target) {
        if(low > high) return -1;
        let mid = low + Math.floor((high-low)/2);
        if(arr[mid] === target) return mid;
        if(arr[low] === target) return low;
        if(arr[high] === target) return high;
        else if(arr[mid] > target) return this.BSR(arr, low, mid-1,target);
        else if(arr[mid] < target) return this.BSR(arr, mid+1, high,target);
    }
    search(arr, target) {
        return this.BSR(arr, 0, arr.length-1, target)
    }
}

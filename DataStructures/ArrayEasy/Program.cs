using System;
using System.Collections.Generic;
using System.Linq;

namespace ArrayEasy
{
    class Program
    {
        static void Main(string[] args)
        {
            var word = "str to Reverse";

            StringReverse.ReverseRecursive(word,word.Length-1);
            //Console.WriteLine("Hello World!");
            //var a = meanMedian(4, new int[4] { 4, 1, 3, 2 });
            //Array.Sort(a);
            //for (int i = 0; i < a.Length; i++)
            //{
            //    Console.Write(a[i]);
            //}
        }

        public static int[] meanMedian(int input1, int[] input2)
        {
             Array.Sort(input2);
            double maxMeanMedian = 0, median, tempMeanMedian;
            int[] maxMeanMedianSubarray = new int[1] { input2[0]}, maxMeanSubarray;

            for (int i = 1; i < (input1 -1 ); i++)
            {
                median = input2[i];
                maxMeanSubarray = getMaxMeanSubarray(i - 1, input1 - 1, i, false, input2);
                tempMeanMedian = ((double)maxMeanSubarray.Sum() / maxMeanSubarray.Length) - median;

                if(tempMeanMedian > maxMeanMedian)
                {
                    maxMeanMedian = tempMeanMedian;
                    maxMeanMedianSubarray = maxMeanSubarray;
                }
            }

            for (int i = 1; i < (input1 - 2); i++)
            {
                median = (input2[i] + input2[i+1]) / 2.0;
                maxMeanSubarray = getMaxMeanSubarray(i - 1, input1 - 1, i, true, input2);
                tempMeanMedian = ((double)maxMeanSubarray.Sum() / maxMeanSubarray.Length) - median;

                if (tempMeanMedian > maxMeanMedian)
                {
                    maxMeanMedian = tempMeanMedian;
                    maxMeanMedianSubarray = maxMeanSubarray;
                }
            }

            return maxMeanMedianSubarray;
        }

        public static int[] getMaxMeanSubarray(int lIndex, int rIndex, int medianIndex, bool isEven, int[] input2)
        {
            double sum=0, maxMean, mean;
            List<int> subarrayList = new List<int>();
            int[] maxMeanSubarray;

            subarrayList.Add(input2[lIndex]);
            subarrayList.Add(input2[rIndex]);
            subarrayList.Add(input2[medianIndex]);

            if (isEven)
            {
                subarrayList.Add(input2[medianIndex+1]);
            }

            maxMeanSubarray = subarrayList.ToArray();

            sum = subarrayList.Sum();
            maxMean = (double)sum / subarrayList.Count;

            lIndex--;
            rIndex--;

            bool keepLooking = lIndex > -1 && ((!isEven && rIndex > medianIndex) || (isEven && rIndex > medianIndex + 1));
            while (keepLooking)
            {
                subarrayList.Add(input2[lIndex]);
                subarrayList.Add(input2[rIndex]);
                sum += input2[lIndex] + input2[rIndex];
                mean = (double)sum / subarrayList.Count;

                if(mean > maxMean)
                {
                    maxMean = mean;
                    maxMeanSubarray = subarrayList.ToArray();
                    keepLooking = lIndex > -1 && ((!isEven && rIndex > medianIndex) || (isEven && rIndex > medianIndex + 1));
                }
                else
                {
                    keepLooking = false;
                }
            }

            return maxMeanSubarray;
        }
    }
}

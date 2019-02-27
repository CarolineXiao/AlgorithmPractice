def substring_with_k_distinct(s, k):
    str_counter = 0
    for i in range(len(s)):
        counter = [0] * 26
        dist_counter = 0
        for j in range(i, len(s)):
            if counter[ord(s[j]) - 97] == 0:
                dist_counter += 1
            counter[ord(s[j]) - 97] += 1
            if dist_counter == k:
                str_counter += 1
            if dist_counter > k:
                break
    return str_counter


if __name__ == "__main__":
  r = substring_with_k_distinct("abcbaa", 3)
  print(r)

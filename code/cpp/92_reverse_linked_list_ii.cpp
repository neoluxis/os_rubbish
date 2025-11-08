/**
 * 92. Reverse Linked List II
 * Given the head of a singly linked list and two integers left and right
 * where left <= right, reverse the nodes of the list from position left to
 * position right, and return the reversed list.
 *
 * Example:
 * Input: head = [1,2,3,4,5], left = 2, right = 4
 * Output: [1,4,3,2,5]
 *
 * Constraints:
 * 1 <= left <= right <= number of nodes
 */

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move prev to the node before the left position
        for (int i = 1; i < left; ++i) {
            prev = prev->next;
        }

        ListNode* curr = prev->next;

        // Reverse the sublist from left to right
        for (int i = 0; i < right - left; ++i) {
            ListNode* nextNode = curr->next;
            curr->next = nextNode->next;
            nextNode->next = prev->next;
            prev->next = nextNode;
        }

        return dummy.next;
    }
};

#ifdef LOCAL_TEST
#include <vector>

ListNode* buildList(const std::vector<int>& vals) {
    if (vals.empty()) return nullptr;
    auto* head = new ListNode(vals[0]);
    ListNode* tail = head;
    for (size_t i = 1; i < vals.size(); ++i) {
        tail->next = new ListNode(vals[i]);
        tail = tail->next;
    }
    return head;
}

void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << (head->next ? " -> " : "");
        head = head->next;
    }
    std::cout << "\n";
}

int main() {
    Solution sol;
    auto* head = buildList({1, 2, 3, 4, 5});
    std::cout << "Original: ";
    printList(head);
    head = sol.reverseBetween(head, 2, 4);
    std::cout << "Reversed (2-4): ";
    printList(head);
    return 0;
}
#endif
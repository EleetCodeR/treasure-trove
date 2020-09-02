#include <bits/stdc++.h>
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl

using namespace std;

class BST
{
public:
    int value;
    BST *left;
    BST *right;

    BST(int val);
    BST &insert(int val);
};

int findClosestValueInBst(BST *tree, int target);
int helper(BST *tree, int target, int &d, int &v);

int findClosestValueInBst(BST *tree, int target)
{
    const int MAX = 1'000'000'007;
    int d = MAX, v = -1;
    int closest = helper(tree, target, d, v);
    return closest;
}
int helper(BST *tree, int target, int &d, int &v)
{
    if (tree)
    {
        cout << "d,v : " << d << "," << v << "\n";
        int k = tree->value;
        int df = abs(target - k);
        cout << "target :" << target << "\n";
        cout << "key :" << k << "\n";
        // check values
        if (d > df)
        {
            d = df;
            v = k;

            cout << "close found :" << v << "\n";
        }
        // traverse bst
        if (target < k)
        {
            //left
            if (tree->left)
            {
                cout << "LST :"
                     << "\n";
                helper(tree->left, target, d, v);
                cout << " LST-v :" << v << "\n";
            }
            else
            {
                return v;
            }
        }
        else
        {
            //right
            if (tree->right)
            {
                cout << "RST :"
                     << "\n";
                helper(tree->right, target, d, v);
                cout << "RST-v :" << v << "\n";
            }
            else
            {
                return v;
            }
        }
    }
    cout << "final ret v :" << v << "\n";
    return v;
}
int main()
{
    // To Avoid input/output bottlenecks
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());

    return 0;
}
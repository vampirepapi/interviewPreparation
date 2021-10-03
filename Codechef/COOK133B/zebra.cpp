#include <bits/stdc++.h>
#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")
using namespace std;
#define int                         long long
#define str                         string
#define ff                          first
#define vec                         vector
#define naturalNumSum(N)            N*(N+1)/2
#define p(x)                        push(x)
const int mod=                      1e9+7;
#define gcd(a,b)                    __gcd(a,b);
#define lcm(a,b)                    a*b/gcd(a,b);
#define pi                          pair
#define ss                          second
#define tc(t)                       while(t--)
#define pb(a)                       push_back(a);
#define endl                        "\n"
#define db                          double
#define clr(a)                      a.clear();
#define fl                          float
#define del                         delete
#define umap                        unordered_map
#define mp                          make_pair
#define ins                         insert
#define stu                         struct
#define vd                          void
#define null                        NULL
#define ppf                         pop_front
#define stk                         stack
#define len(string)                 string.length()
#define print(a)                    cout<<a<<endl;
#define lb                          lower_bound
#define ub                          upper_bound
#define printArr(arr)               for(auto &i : arr){cout<<i<<" ";}
#define printMap(m)                 for(auto &v : m){cout<<v.ff<<" "<<v.ss<<endl;}
#define ll long long
//structural node
stu Node{
    int data;
    stu Node* left;
    stu Node* right;
    Node(int val){
        data = val;
        left=null;
        right=null;
    }
};

// linked list codes

class node{
    public:
        int data;
        node* next;
        node(int val){
            data=val;
            next=null;
        }
};
vd insatTail(node* &head, int val){
    node* n= new node(val);
    if(head==null){
        head=n;
        return;
    }
    node* temp=head;
    while(temp -> next !=null){
        temp=temp->next;
    }
    temp->next=n;
}
vd display(node* head){
    node* temp=head;
    while(temp!=null){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}
vd insatHead(node* &head,int val){
    node* n= new node(val);
    n->next=head;
    head=n;
}
bool search(node* head,int key){
    node* temp=head;
    while(temp!=null){
        if(temp->data==key){
            return true;
        }
        temp=temp->next;
    }
    return false;
}
vd delHead(node* &head){
    node* todel=head;
    head=head->next;
    del todel;
}
vd deletion(node* &head, int val){
    node* temp=head;
    while(temp->next->data != val){
        temp=temp->next;
    }
    node* todel= temp->next;
    temp->next=temp->next->next;
    del todel;
}
/*
    *IMPLEMENTAIONS*
        INSERT AT TAIL
            *insatTail(head, value)
        INSERT AT HEAD
            *insatHead(head, value)
        DELETE AN ELEMENT
            
*/
//linked list code end

vd sol(){
    node* head=null;
    insatTail(head,1);insatTail(head,2);
    insatTail(head,3);insatHead(head,4);
    display(head);
    deletion(head,2);
    delHead(head);
    display(head);

}
void solve()
{
    ll n,k;
    cin>>n>>k;
    string str;
    cin>>str;

    char res = str[0];
    int cnt =0;
    for(int i=1;i<n;i++) {
        if(res != str[i]) {
            cnt++;
            res = str[i];
        }
    }

    if(cnt<k) {
        cout<<-1<<"\n";
        return;
    }
    if(str[0]=='0') {
        if(k%2) {
            for(int i=str.size()-1; i>=0; i--) {
                if(str[i] == '1') {
                    cout<<i+1<<"\n";
                    return;
                }
            }
        }
        else {
            for(int i=str.size()-1; i>=0; i--) {
                if(str[i] == '0') {
                    cout<<i+1<<"\n";
                    return;
                }
            }
        }
    }
    else {
        if(k%2) {
            for(int i=str.size()-1; i>=0; i--) {
                if(str[i] == '0') {
                    cout<<i+1<<"\n";
                    return;
                }
            }
        }
        else {
            for(int i=str.size()-1; i>=0; i--) {
                if(str[i] == '1') {
                    cout<<i+1<<"\n";
                    return;
                }
            }
        }
    }

}
main()
{
    //fast input and output
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int T;
    cin>>T;
    while(T--) {
        solve();
    }
    return 0;
}
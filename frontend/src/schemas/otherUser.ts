// 看要寫在 user 還是拉出來寫
export interface OtherUser {
    uid: string,
    name: string,
    role: string,
    department: string,
};

export interface OtherUserContent extends OtherUser{
    country: string,
    email: string,
    introduction: string,
}

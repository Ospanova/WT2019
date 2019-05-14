
export interface IPost {
    id: number;
    title: string;
    body: string;
    like_count: number;
    created_at: Date;
    created_by: User
}
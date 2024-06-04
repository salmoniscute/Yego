export interface WebAnnouncementInfo {
    id: number;
    publisher: string;
    release_time: string;
    title: string;
    pin_to_top: boolean;
}

export interface WebAnnouncementContent extends WebAnnouncementInfo {
    content: string,
    publisher: string,
    files?: Array<string>,
}
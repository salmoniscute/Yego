export interface Notification {
  uid: string,
  release_time: string,
  title: string,
  content: string
}

export interface NotificationCreate {
  have_read: Boolean,
  release_time: string,
  type: string
}

export interface NotificationRead {
  id: number,
  publisher: string,
  course_name: string,
  release_time: string,
  title: string,
  content: string,
  have_read: string,
  icon_type: string,
}  

export interface NotificationUpdate {
  have_read: Boolean
}  

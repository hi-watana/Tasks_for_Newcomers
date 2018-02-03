#!/usr/local/bin/gosh
(define average
  (lambda lst (/ (exact->inexact (apply + lst)) (length lst))))

(define (my-string->number s)
  (string->number (string-trim-both s)))

(define (main args)
  (use srfi-13)
  (cond ((not (= (length args) 3))
         (display
           (string-append "Usage: " (car args) " <PDB file> <chain name>\n"))
         (exit 1)))
  (let* ((atom-line?
           (lambda (s)
             (and (or (equal? (substring s 0 4) "ATOM")
                      (equal? (substring s 0 6) "HETATM"))
                  (equal? (substring s 13 15) "CA")
                  (let ((altLoc (substring s 15 16)))
                    (or (equal? altLoc " ")
                        (equal? altLoc "A")))
                  (equal? (substring s 21 22) (caddr args)))
             ))
         (atom-list (call-with-input-file
                      (cadr args)
                      (lambda (s)
                        (filter atom-line? (port->string-list s)))))
         (xyz-list
           (map (lambda (s)
                  (list (my-string->number (substring s 30 37))
                        (my-string->number (substring s 38 45))
                        (my-string->number (substring s 46 53))))
                atom-list))
         (center-of-gravity (apply map average xyz-list))
         (relative-xyz-list (map (lambda (xyz)
                                   (map - xyz center-of-gravity))
                                 xyz-list))
         (radius-list (map (lambda (xyz)
                             (sqrt (apply + (map * xyz xyz))))
                           relative-xyz-list))
         (radius-average (apply average radius-list)))
    (display radius-average)
    (newline)) 0)
